import React, { useState } from "react";
import "./css/main.css";

function App() {
  const [response, setResponse] = useState("Waiting for your input...");
  const [question, setQuestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResponse("Loading...");
    try {
const res = await fetch("http://localhost:8000/api/nlp/query", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: question }),
});
const data = await res.json();
setResponse(
  `Procedure: ${data.procedure || "N/A"}, Location: ${data.location || "N/A"}, Insurance: ${data.insurance || "N/A"}`
);
    } catch (error) {
      setResponse("An error occurred. Please try again.");
    }
  };

  return (
    <div className="container">
      <h1>Healthcare Helper</h1>
      <form className="form" onSubmit={handleSubmit}>
        <label htmlFor="insurance-upload" className="upload-label">
          Please upload your health insurance document (PDF, JPG, or PNG).
        </label>
        <input
          type="file"
          id="insurance-upload"
          name="insurance"
          accept=".pdf,.jpg,.jpeg,.png"
        />
        <textarea
          rows="6"
          placeholder="Describe your healthcare concern or question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        ></textarea>
        <button type="submit">Submit</button>
      </form>
      <div className="response-card">
        {response}
      </div>
    </div>
  );
}

export default App;