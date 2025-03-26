export function taskFirst() {
    const task = false;  // Default value for task
    const task2 = true;  // Default value for task2
    return [task, task2];
  }
  
  export function taskConditional(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    // Only modify task and task2 if the condition is true
    if (trueOrFalse) {
      task = true;
      task2 = false;
    }
  
    return [task, task2];
  }
  
  export function taskNext(trueOrFalse) {
    const initialTasks = taskFirst();  // Get default values
    const modifiedTasks = taskConditional(trueOrFalse);  // Modify if needed
    return modifiedTasks;
  }
  