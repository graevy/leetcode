use std::collections::HashMap;
use std::collections::HashSet;

let mut solutions = HashMap::new();


pub fn is_factorable(candidates: Vec<i32>, target i32) {
    TODO
}

pub fn recur(candidates: Vec<i32>, target: i32) {
    let mut remainders = HashSet::new();
    // TODO: hash all candidates for faster membership checking?
    let mut members = HashSet::new();

    Vec<Vec<i32>> output;
    candidates.sort();


    for n in candidates {
        if target % n in members {
            let combination = Vec<i32>[n for x in range(target INTDIV n)]
            output.insert(combination)
        }
        else if len(recur(candidates,target%n)) > 0 {
            TODO
        }

    }
}

fn main() {
    recur(candidates, target)
}

// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

// It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


// 1 <= candidates.length <= 30
// 1 <= candidates[i] <= 200
// All elements of candidates are distinct.
// 1 <= target <= 500

// notes:
// if target is 6, and candidates is [1,2,3] we need:
// [[1,1,1,1,1,1], [1,1,1,1,2], [1,1,2,2], [1,1,1,3], [1,2,3], [2,2,2], [3,3]]
