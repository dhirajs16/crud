
const Form = () => {

    const handleFormSubmit = (e) => {
        e.preventDefault()
    }
  return (
    <>
        <form onSubmit={handleFormSubmit} className="flex flex-col gap-5 text-gray-900">
        <input type="text" name="title" id="id_title" placeholder="Enter book title" className="rounded-xl px-3 py-1"/>
        <input type="text" name="release_year" id="id_release_year" placeholder="Enter release year" className="rounded-xl px-3 py-1" />
        <button type="submit" className="bg-gray-800 rounded-xl px-3 py-1 text-white">Submit</button>
      </form>
    </>
  )
}

export default Form