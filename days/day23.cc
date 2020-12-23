#include <algorithm>
#include <iostream>
#include <string>

#define N 1000000
#define N_MOVES 10000000

struct Node {
  uint64_t val;
  Node *next;
};

class Array {
  Node *first;
  Node *values[N+1];
  uint64_t cur_cup;

public:
  Array(const std::string &init) {
    first = new Node[N];
    for (int i = 0; i < init.size(); ++i) {
      uint64_t val = (uint64_t)init[i] - (uint64_t)'0';
      first[i].val = val;
      first[i].next = first + i + 1;
      values[val] = first + i;
    }

    uint64_t max = *std::max_element(init.data(), init.data() + init.size()) -
                   (uint64_t)'0';
    size_t size = init.size();

    for (int i = 0; i < N - size; ++i) {
      uint64_t val = max + i + 1;
      Node *ptr = first + i + size + 1;
      first[i + size].val = val;
      first[i + size].next = ptr;
      values[val] = first + i + size;
    }

    values[N]->next = first;
    cur_cup = first->val;
  }

  uint64_t next_dest() {
    uint64_t vals[3];
    Node *cur = values[cur_cup]->next;
    for (int i = 0; i < 3; ++i) {
      vals[i] = cur->val;
      cur = cur->next;
    }

    uint64_t new_dest = cur_cup;
    do {
      new_dest = new_dest - 1;
      if (new_dest == 0)
        new_dest = N;
    } while (new_dest == vals[0] || new_dest == vals[1] || new_dest == vals[2]);
    return new_dest;
  }

  void swap(uint64_t new_dest) {
    Node *first = values[cur_cup]->next;
    Node *last_slice = first->next->next;
    Node *last = last_slice->next;
    Node *new_last_slice = values[new_dest]->next;

    values[cur_cup]->next = last;
    values[new_dest]->next = first;
    last_slice->next = new_last_slice;

		cur_cup = last->val;
  }

  uint64_t sol() {
    Node *one_ptr = values[1];
    return one_ptr->next->val * one_ptr->next->next->val;
  }

  ~Array() { delete[] first; }
};

int main() {
  Array array = Array("716892543");

  for (int i = 0; i < N_MOVES; ++i) {
    uint64_t new_dest = array.next_dest();
    array.swap(new_dest);
  }

  std::cout << "sol: " << array.sol() << std::endl;

  exit(EXIT_SUCCESS);
}
