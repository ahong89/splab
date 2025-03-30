import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Bill = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const navigate = useNavigate();

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      setSelectedImage(imageUrl);
    }
  };

  const handleCancel = () => {
    setSelectedImage(null);
  };

  const handleProceed = () => {
    navigate("/confirm-upload"); 
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h2 className="text-2xl font-semibold mb-6">Upload your bill</h2>

      {!selectedImage ? (
        <label className="w-full flex flex-col items-center justify-center bg-white p-6 rounded-xl shadow-md cursor-pointer">
          <span className="text-gray-500 mb-2">Tap to take a picture or upload</span>
          <input
            type="file"
            accept="image/*"
            capture="environment"
            className="hidden"
            onChange={handleImageChange}
          />
        </label>
      ) : (
        <div className="w-full flex flex-col items-center gap-4">
          <img
            src={selectedImage}
            alt="Uploaded bill"
            className="w-full max-w-xs rounded-xl shadow-md"
          />
          <div className="flex gap-4 mt-6">
            <button
              onClick={handleCancel}
              className="px-4 py-2 bg-red-500 text-white rounded-full shadow hover:bg-red-600 transition"
            >
              Cancel
            </button>
            <button
              onClick={handleProceed}
              className="px-4 py-2 bg-green-500 text-white rounded-full shadow hover:bg-green-600 transition"
            >
              Proceed
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Bill;
