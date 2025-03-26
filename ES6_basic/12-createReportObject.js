export default function createReportObject(employeesList) {
    return {
      allEmployees: { ...employeesList }, // Spread the employeesList to avoid direct mutation
      getNumberOfDepartments: function() {
        return Object.keys(employeesList).length; // Count the number of keys in the employeesList (departments)
      }
    };
  }
  