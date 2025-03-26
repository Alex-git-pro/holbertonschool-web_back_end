export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      let task = true;  // This 'task' variable is scoped inside the if block
      let task2 = false;  // This 'task2' variable is also scoped inside the if block
    }
  
    return [task, task2];  // Return the original 'task' and 'task2' values
  }
  