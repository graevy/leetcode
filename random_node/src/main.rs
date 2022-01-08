// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

use rand::Rng;
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(head: Option<Box<ListNode>>) -> Self {
        
    }
    
    fn get_random(&self) -> i32 {

        ListNode result;
        let mut current_node = head;
        let mut rng = rand::thread_rng();
        let mut count: i32 = 0;
        while result.next != None {
            if rng.gen_range(0..count) < 1 {
                result = current_node;
            }
        }
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(head);
 * let ret_1: i32 = obj.get_random();
 */

/**
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.count = 1
        self.res = None
        self.node = head

    def getRandom(self) -> int:
        while self.node.next != None:
            if random.uniform(0,count) < 1:
                self.res = self.node.val
            self.node = self.node.next
            count += 1
**/

fn main() {
    println!("Hello, world!");
}
