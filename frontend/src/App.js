import React, { useState } from "react";
import "./css/main.css";

function App() {
  const [response, setResponse] = useState("Waiting for your input...");
  const [recommendations, setRecommendations] = useState([]);
  const [costSummary, setCostSummary] = useState(null);
  const [question, setQuestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResponse("Loading...");
    setRecommendations([]);
    setCostSummary(null);
    try {
  const res = await fetch("https://healthcare-helper.onrender.com/api/nlp/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: question }),
      });
      const data = await res.json();
      if (data.response) {
        setResponse("Here are your recommendations:");
        setRecommendations(data.response.recommendations || []);
        setCostSummary(data.response.cost_summary || null);
      } else if (data.error) {
        setResponse(data.error);
      } else {
        setResponse("No recommendations found.");
      }
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
        <p>{response}</p>
        {recommendations.length > 0 && (
          <div>
            <h3>Recommendations:</h3>
            <ul>
              {recommendations.map((rec, idx) => (
                <li key={idx}>
                  <strong>{rec.procedure_name}</strong> at {rec.provider_name} ({rec.location})<br />
                  Cost: ${rec.patient_pays}<br />
                  Quality: {rec.quality_rating}/5<br />
                  Relevance: {rec.relevance_score}
                </li>
              ))}
            </ul>
          </div>
        )}
        {costSummary && (
          <div>
            <h3>Cost Summary:</h3>
            <pre>{JSON.stringify(costSummary, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;