// taskFirst function: Use const since 'task' is not reassigned.
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // Helper function that returns a string
  export function getLast() {
    return ' is okay';
  }
  
  // taskNext function: Use let since 'combination' is reassigned.
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();  // 'combination' is reassigned here
  
    return combination;
  }
  