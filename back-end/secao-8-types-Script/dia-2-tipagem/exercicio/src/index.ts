import Author from './database/models/AuthorModel';
import Book from './database/models/BookModel';
import Genre from './database/models/GenresModel';
// (async () => {
//   const authors = await Author.findAll();
//   console.table(authors.map((author) => author.toJSON()));

//   process.exit(0);
// })();

// (async () => {
//   const books = await Book.findAll();
//   console.table(books.map((book) => book.toJSON()));

//   process.exit(0);
// })();

(async () => {
  const data = await Author.findAll({
    include: {
      model: Book,
      attributes: [],
    },
    attributes: [
      ['name', 'author'],
      // [sequelize.fn('COUNT', sequelize.col('books.id')), 'totalBooks'],
    ],
    group: 'authors.name',
    order: [['totalBooks', 'DESC']],
    raw: true,
  });

  console.log(data);
  process.exit(0);
})();