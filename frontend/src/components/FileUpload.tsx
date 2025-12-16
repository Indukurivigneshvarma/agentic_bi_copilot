import { useState } from "react";
import { uploadFile } from "../services/api";

interface Props {
  onSuccess: () => void;
}

const FileUpload = ({ onSuccess }: Props) => {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    try {
      setMessage("Uploading...");

      const res = await uploadFile(file);
      console.log("UPLOAD RESPONSE:", res);

      // 🔴 THIS CHECK IS CRITICAL
      if (res && (res.status === "success" || res.status === "accepted")) {
        setMessage("Upload successful");
        onSuccess(); // 🔥 THIS WAS NOT FIRING BEFORE
      } else {
        setMessage("Upload failed");
      }
    } catch (err) {
      console.error(err);
      setMessage("Upload error");
    }
  };

  return (
    <div className="card">
      <input
        type="file"
        accept=".xlsx,.xls"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />
      <button onClick={handleUpload}>Upload</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default FileUpload;
