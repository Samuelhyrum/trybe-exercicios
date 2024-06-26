const books = [
  {
    id: 1,
    name: 'As Crônicas de Gelo e Fogo',
    genre: 'Fantasia',
    author: {
      name: 'George R. R. Martin',
      birthYear: 1948,
    },
    releaseYear: 1991,
  },
  {
    id: 2,
    name: 'O Senhor dos Anéis',
    genre: 'Fantasia',
    author: {
      name: 'J. R. R. Tolkien',
      birthYear: 1892,
    },
    releaseYear: 1954,
  },
  {
    id: 3,
    name: 'Fundação',
    genre: 'Ficção Científica',
    author: {
      name: 'Isaac Asimov',
      birthYear: 1929,
    },
    releaseYear: 1951,
  },
  {
    id: 4,
    name: 'Duna',
    genre: 'Ficção Científica',
    author: {
      name: 'Frank Herbert',
      birthYear: 1920,
    },
    releaseYear: 1965,
  },
  {
    id: 5,
    name: 'A Coisa',
    genre: 'Terror',
    author: {
      name: 'Stephen King',
      birthYear: 1947,
    },
    releaseYear: 1986,
  },
  {
    id: 6,
    name: 'O Chamado de Cthulhu',
    genre: 'Terror',
    author: {
      name: 'H. P. Lovecraft',
      birthYear: 1890,
    },
    releaseYear: 1928,
  },
];

// //Primeiro exercicio
// const authorBornIn1947 = books.find(book => book.author.birthYear === 1947);

// console.log(authorBornIn1947);


//Segundo Exercicio 
// var tamanho = 'O Chamado de Cthulhu';
// function smallerName() {
//   let nameBook = 'O Chamado de Cthulhu';
//   books.forEach((book) => {
//     if (book.name.length < nameBook.length) {
//       nameBook = book.name;
//   }})
//   return nameBook;
// }
// console.log(smallerName());



//Terceiro exercicio

// const getNamedBook = books.find((b)=> b.name.length === 26);
// console.log(getNamedBook);


// Quarto exercicio

// books.sort((a,b)=> a.releaseYear < b.releaseYear ? 1 : -1)
// console.log(books);



//Quinto exercicio
// const everyoneWasBornOnSecXX = books.every((born)=> born.author.birthYear <=1999 )
// console.log(everyoneWasBornOnSecXX);


// Sexto Exercicio
// const onthe80s = books.some((oitenta) => oitenta.releaseYear <= 1990 && oitenta.releaseYear >= 1980)
// console.log(onthe80s);


// Sétimo Exercicio

const authorUnique =(book, ano) => book.every((book)=> book.author.birthYear !== ano );

console.log(authorUnique(books, 1920));









// function authorUnique() {
//   let nascido = 1919;
//   let boleano;
//   books.forEach((book) => {
//     if (book.author.birthYear.includes(nascido)) {
//       nascido = book.author.birthYear;
//       boleano = false;
//     } else boleano = true;
//   })
//   return boleano;
// }

// console.log(authorUnique());