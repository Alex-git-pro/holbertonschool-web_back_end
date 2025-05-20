const fs = require("fs");

function countStudents(filePath) {
  try {
    const data = fs.readFileSync(path.resolve(filePath), "utf8");

    const lines = data.split("\n").filter((line) => line.trim() !== "");
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};

    students.forEach((line) => {
      const parts = line.split(",");
      const firstName = parts[0];
      const field = parts[3];

      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    });

    for (const field in fields) {
      const list = fields[field];
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(
          ", ",
        )}`,
      );
    }
  } catch (err) {
    throw new Error("Cannot load the database");
  }
}

module.exports = countStudents;
