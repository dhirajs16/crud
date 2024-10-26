

const BookList = ({ books }) => {
    
    return (
        <div>
            <h3 className="text-3xl font-bold text-center">List</h3>
            {books.map((book, index) => (
                <div className="flex justify-between gap-5" key={index}>
                    <h3>{book.title}</h3>
                    <h3>{book.release_year}</h3>
                </div>
            ))}
        </div>
    );
}

export default BookList;
