export default function Dashboard() {
  const students = [
    { name: 'Rahul', marks: 78, attendance: 85, hours: 4 },
    { name: 'Sneha', marks: 88, attendance: 90, hours: 5 },
    { name: 'Amit', marks: 67, attendance: 75, hours: 3 },
    { name: 'Priya', marks: 92, attendance: 95, hours: 6 },
    { name: 'Karan', marks: 74, attendance: 80, hours: 4 },
  ];

  const avgMarks = (
    students.reduce((sum, s) => sum + s.marks, 0) / students.length
  ).toFixed(1);

  const avgAttendance = (
    students.reduce((sum, s) => sum + s.attendance, 0) / students.length
  ).toFixed(1);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-4xl font-bold text-center mb-8 text-blue-700">
        Student Data Cleaning & Visualization Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
          <h2 className="text-xl font-semibold text-gray-700">Total Students</h2>
          <p className="text-4xl font-bold text-blue-600 mt-3">5</p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
          <h2 className="text-xl font-semibold text-gray-700">Average Marks</h2>
          <p className="text-4xl font-bold text-green-600 mt-3">{avgMarks}</p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6 text-center">
          <h2 className="text-xl font-semibold text-gray-700">Average Attendance</h2>
          <p className="text-4xl font-bold text-purple-600 mt-3">{avgAttendance}%</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 overflow-x-auto">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">Student Performance Table</h2>

        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-blue-100">
              <th className="border p-3">Name</th>
              <th className="border p-3">Marks</th>
              <th className="border p-3">Attendance</th>
              <th className="border p-3">Study Hours</th>
            </tr>
          </thead>

          <tbody>
            {students.map((student, index) => (
              <tr key={index} className="text-center hover:bg-gray-100">
                <td className="border p-3">{student.name}</td>
                <td className="border p-3">{student.marks}</td>
                <td className="border p-3">{student.attendance}%</td>
                <td className="border p-3">{student.hours} hrs</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h2 className="text-2xl font-bold mb-6 text-blue-700">Marks Visualization</h2>

          {students.map((student, index) => (
            <div key={index} className="mb-4">
              <div className="flex justify-between mb-1">
                <span className="font-medium">{student.name}</span>
                <span>{student.marks}</span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-5">
                <div
                  className="bg-blue-600 h-5 rounded-full"
                  style={{ width: `${student.marks}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h2 className="text-2xl font-bold mb-6 text-green-700">Attendance Visualization</h2>

          {students.map((student, index) => (
            <div key={index} className="mb-4">
              <div className="flex justify-between mb-1">
                <span className="font-medium">{student.name}</span>
                <span>{student.attendance}%</span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-5">
                <div
                  className="bg-green-600 h-5 rounded-full"
                  style={{ width: `${student.attendance}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow-lg p-6 mt-8">
        <h2 className="text-2xl font-bold text-blue-700 mb-4">Project Summary</h2>

        <ul className="list-disc pl-6 space-y-2 text-gray-700 text-lg">
          <li>Missing values and duplicate records were cleaned using Python.</li>
          <li>Student performance data was analyzed successfully.</li>
          <li>Visual reports were created for better understanding.</li>
          <li>Higher study hours showed better academic performance.</li>
        </ul>
      </div>
    </div>
  );
}
