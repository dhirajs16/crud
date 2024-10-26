import { useEffect, useState } from "react";
import Form from "./components/Form";
import BookList from "./components/BookList";

const App = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/books/");
      const data = await response.json()
      setBooks(data)
    } catch (error) {
      console.log("Fetching error:", error);
    }
  };



  return (
    <div className="flex flex-col justify-center items-center h-screen gap-5">
      <h3 className="font-bold text-5xl">Books Website</h3>
      <Form />
      <BookList books = {books} />
    </div>
  );
};

export default App;
