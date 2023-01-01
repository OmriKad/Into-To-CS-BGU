from functools import total_ordering
from msilib import sequence


class ByteNode:
    def __init__(self, byte):
        """
        Creating ByteNodes, only strings representing a byte are accepted.
        :param byte:
        """
        try:
            if type(byte) != str:
                raise TypeError('The given byte is not made of strings!')
            else:
                counter = 0
                for i in byte:
                    counter += 1
                    if int(i) >= 2:
                        raise ValueError('A byte length is 8 and is a binary animal, only 1 or 0 is acceptable.')
                if counter != 8:
                    raise ValueError('A byte length is 8 and is a binary animal, only 1 or 0 is acceptable.')
        finally:
            self.byte = byte
            self.next = None

    def get_byte(self):
        return self.byte

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return f'[{self.byte}]=>'


@total_ordering
class LinkedListBinaryNum:
    def __init__(self, num=0):
        """
        Creating a LinkedList made of ByteNodes. Only a positive integer is accepted. The integer is being transformed
        into a binary strings using math, then each is sent to the add MSB method for linking.
        :param num:
        """
        if num < 0:
            raise ValueError('Given num must be greater or equal to zero.')
        elif type(num) != int:
            raise TypeError('Given num must be an int.')
        self.size = 0
        self.head = None
        # Converting to a Binary num
        st = ''
        counter = 0
        while num:
            counter += 1
            st = str(num % 2) + st
            num = num // 2
        # Filling with zeros in cases of not a full Byte
        if st == '':
            st = '00000000'
        mod = counter % 8
        if mod != 0:
            st = (8 - mod) * '0' + st
            length = counter + (8 - mod)
        # ByteNode making
        else:
            length = len(st)
        for i in range(length // 8):
            self.add_MSB(st[-8:])
            st = st[:-8]

    def add_MSB(self, byte):
        msb = ByteNode(byte)
        if self.size == 0:
            self.head = msb
        else:
            tmp = self.head
            self.head = msb
            self.head.set_next(tmp)
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):  # end user
        final = '|'
        p = self.head
        while p is not None:
            final += f'{p.byte}|'
            p = p.next
        return final

    def __repr__(self):  # developer
        map = ''
        p = self.head
        while p is not None:
            map += str(p)
            p = p.next
        map += 'None'
        if self.size == 1:
            final = f'LinkedListBinaryNum with 1 Byte, Bytes map: {map}'
        else:
            final = f'LinkedListBinaryNum with {self.size} Bytes, Bytes map: {map}'
        return final

    def __getitem__(self, item):
        if type(item) != int:
            raise TypeError
        elif item >= self.size or item <= -self.size - 1:
            raise IndexError
        else:
            p = self.head
            if item >= 0:
                for i in range(0, item):
                    p = p.next
                return p.byte
            else:
                for i in range(0, self.size + item):
                    p = p.next
                return p.byte

    # Order relations:
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

    def __lt__(self, other):
        a = str(self)
        a = a.replace('|', '')
        b = str(other)
        b = b.replace('|', '')
        if len(a) < len(b):
            a = str(('0' * (len(b) - len(a)))) + a
        if len(b) < len(a):
            b = str(('0' * (len(a) - len(b)))) + b
        for x, y in zip(a, b):
            if x < y:
                return True
            if x > y:
                return False

    def __add__(self, other):
        if type(other) == int:
            if other < 0:
                raise ValueError
            else:
                return self.__add__(LinkedListBinaryNum(other))
        if type(other) != LinkedListBinaryNum:
            raise TypeError
        # trimmed version of self
        a = str(self)
        a = a.replace('|', '')
        trimmed_a = str(a[::-1].rstrip('0'))[::-1]
        trimmed_a_len = len(trimmed_a)
        # trimmed version of other
        b = str(other)
        b = b.replace('|', '')
        trimmed_b = str(b[::-1].rstrip('0'))[::-1]
        trimmed_b_len = len(trimmed_b)
        # comparing both len of trimmed versions. if one is less than the other, 0's are filled
        if trimmed_a_len < trimmed_b_len:
            trimmed_a = str(('0' * (trimmed_b_len - trimmed_a_len))) + trimmed_a
        if trimmed_b_len < trimmed_a_len:
            trimmed_b = str(('0' * (trimmed_a_len - trimmed_b_len))) + trimmed_b
        # addition of both trimmed numbers using binary addition rules
        final = ''
        addition = 0
        carry = 0
        i = len(trimmed_a) - 1
        while i >= 0:
            addition = carry
            if i >= 0:
                addition += int(trimmed_a[i]) + int(trimmed_b[i])
            final += str(addition % 2)
            carry = int(addition / 2)
            trimmed_a = trimmed_a[:-1]
            trimmed_b = trimmed_b[:-1]
            i += -1
        if carry != 0:
            final += '1'
        final = final[::-1]
        # creation of new LinkedListBinaryNum object based on new sum
        return LinkedListBinaryNum(int(final, 2))

    def __sub__(self, other):
        if type(other) == int:
            if other < 0:
                raise ValueError
            if LinkedListBinaryNum(other) > self:
                raise ValueError
            else:
                return self.__sub__(LinkedListBinaryNum(other))
        if type(other) == LinkedListBinaryNum:
            if other > self:
                raise ValueError
        if type(other) != LinkedListBinaryNum:
            raise TypeError
        # trimmed version of self
        a = str(self)
        a = a.replace('|', '')
        trimmed_a = str(a[::-1].rstrip('0'))[::-1]
        trimmed_a_len = len(trimmed_a)
        # trimmed version of other
        b = str(other)
        b = b.replace('|', '')
        trimmed_b = str(b[::-1].rstrip('0'))[::-1]
        trimmed_b_len = len(trimmed_b)
        # comparing both len of trimmed versions. if one is less than the other, 0's are filled
        if trimmed_a_len < trimmed_b_len:
            trimmed_a = str(('0' * (trimmed_b_len - trimmed_a_len))) + trimmed_a
        if trimmed_b_len < trimmed_a_len:
            trimmed_b = str(('0' * (trimmed_a_len - trimmed_b_len))) + trimmed_b
        # subtraction of both trimmed numbers using 2's complement for negative binary nums
        final = ''
        for i in trimmed_b:
            if i == '1':
                final += '0'
            else:
                final += '1'
        trimmed_b = '0' + final
        z = str((len(trimmed_b) - 1) * '0' + '1')
        final = ''
        addition = 0
        carry = 0
        i = len(trimmed_b) - 1
        while i >= 0:
            addition = carry
            if i >= 0:
                addition += int(z[i])
                addition += int(trimmed_b[i])
            final += str(addition % 2)
            carry = int(addition / 2)
            z = z[:-1]
            trimmed_b = trimmed_b[:-1]
            i -= 1
        if carry != 0:
            final += '1'
        trimmed_b = final[::-1]
        trimmed_a = str((len(trimmed_b) - len(trimmed_a)) * '0') + trimmed_a
        final = ''
        addition = 0
        carry = 0
        i = len(trimmed_b) - 1
        while i >= 0:
            addition = carry
            if i >= 0:
                addition += int(trimmed_a[i])
                addition += int(trimmed_b[i])
            final += str(addition % 2)
            carry = int(addition / 2)
            trimmed_a = trimmed_a[:-1]
            trimmed_b = trimmed_b[:-1]
            i -= 1
        if carry != 0:
            final += '1'
        final = final[::-1]
        return LinkedListBinaryNum(int(final[1:], 2))

    def __radd__(self, other):
        return self + other


class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next
        if next is not None:
            next.prev = self

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev
        if prev is not None:
            prev.next = self

    def __repr__(self):
        return f'=>[{self.get_data()}]<='


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_at_start(self, data):
        self.size += 1
        new_node = DoublyLinkedNode(data)
        if self.size == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_prev(new_node)
            self.head = new_node

    def remove_from_end(self):
        if self.is_empty():
            raise StopIteration
        end = self.tail.get_data()
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        self.size += -1
        return end

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def __repr__(self):
        if self.is_empty():
            return 'Head==><==Tail'
        else:
            res = 'Head='
            i = self.head
            while i:
                res += str(i)
                i = i.get_next()
            return res + '=Tail'

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False


class DoublyLinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, val):
        self.data.add_at_start(val)

    def dequeue(self):
        return self.data.remove_from_end()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def __repr__(self):
        if self.is_empty():
            return 'Newest=>[]<=Oldest'
        else:
            final = ']<=Oldest'
            temp = ''
            for i in self:
                temp = ',' + str(i) + temp
            final = 'Newest=>[' + temp[1:] + final
            return final

    def __iter__(self):
        self.current = self.data.get_tail()
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        res = self.current.get_data()
        self.current = self.current.get_prev()
        return res


from hw8_lib import Stack
from hw8_lib import BinarySearchTree


class NumsManagment:
    def __init__(self, file_name):
        self.file_name = file_name

    def is_line_pos_int(self, st):
        st = st[:-1]
        if not st.isdigit():
            return False
        st = float(st)
        if st % 1 == 0 and st > 0:
            return True
        else:
            return False

    def read_file_gen(self):
        try:
            file = open(self.file_name)
            for x in file:
                if self.is_line_pos_int(x):
                    x = LinkedListBinaryNum(int(x))
                    yield x
        except Exception:
            raise FileNotFoundError
        finally:
            file.close()

    def stack_from_file(self):
        gen = self.read_file_gen()
        stack = Stack()
        while True:
            try:
                stack.push(next(gen))
            except StopIteration:
                return stack

    def sort_stack_descending(self, s):
        final_stack = Stack()
        while len(s) != 0:
            temp = s.pop()
            while len(final_stack) != 0 and final_stack.top() > temp:
                s.push(final_stack.pop())
            final_stack.push(temp)
        return final_stack

    def queue_from_file(self):
        gen = self.read_file_gen()
        queue = DoublyLinkedListQueue()
        while True:
            try:
                queue.enqueue(next(gen))
            except StopIteration:
                return queue

    def set_of_bytes(self, q_of_nums):
        final_set = set()
        for i in q_of_nums:
            for j in i:
                final_set.add(j)
        return final_set

    def nums_bst(self):
        pass

    def bst_closest_gen(self, bst):
        pass
