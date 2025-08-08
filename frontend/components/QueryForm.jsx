import React from 'react';

function QueryForm() {
  return (
    <form className="form">
      <label htmlFor="insurance-upload" className="upload-label">
        📄 Please upload your health insurance document (PDF, JPG, or PNG).
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
  );
}

export default QueryForm;
