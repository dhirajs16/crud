import axios from "axios";
import { useState } from "react";

const App = () => {
  const [id, setId] = useState(0);

  const handleGetAll = async () => {
    const getData = await axios.get("http://127.0.0.1:8000/api/");
    console.log(getData.data);
  };

  const handlePost = async () => {
    const postData = {
      name: "Shivam",
      roll: 1011,
      city: "Shivpur",
    };
    const response = await axios.post("http://127.0.0.1:8000/api/", postData);
    console.log(response);
  };

  const handleGet = async (e) => {
    e.preventDefault();
    if (id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/7`);
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    } else {
      console.error("Please enter a valid ID");
    }
  };

  return (
    <>
      <div>App</div>
      <button onClick={handleGetAll}>Get All Data</button>
      <button onClick={handlePost}>Post Data</button>
      <hr />
      <form onSubmit={handleGet}>
        <input
          value={id}
          onChange={(e) => setId(e.target.value)}
          type="number"
          name="id"
          id="id_id"
        />
        <button type="submit">Get Data</button>
      </form>
    </>
  );
};

export default App;
