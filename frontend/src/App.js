import React from "react";
import "./css/main.css";

function App() {
  return (
    <div className="container">
      <h1>Healthcare Helper</h1>
      <form className="form">
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
        ></textarea>
        <button type="submit">Submit</button>
      </form>
      <div className="response-card">
        {/* AI-generated response will appear here */}
        Waiting for your input...
      </div>
    </div>
  );
}

export default App;