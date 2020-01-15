## WEEK 4 - WORKSHOP: Coding Etiquette

It's always delightful to start with the masters, and there is no larger master in this area than [Don Knuth](https://www.nytimes.com/2018/12/17/science/donald-knuth-computers-algorithms-programming.html). You may have heard his name because he's authored the still ongoing collection of books - [The Art of Computer Programming](https://www-cs-faculty.stanford.edu/~knuth/taocp.html). Let's begin this week by reading his 1974 ACM Turing Award Lecture - [__Computer Programming as an Art__](https://dl.acm.org/ft_gateway.cfm?id=1283929&type=pdf). An incredibly thoughtful and scholarly view of what coding is - and should be - all about:

> computer programming is an art, because it applies accumulated knowledge to the world, because it requires skill and ingenuity, and especially because it produces objects of beauty.

With that background, we can jump directly to reading about coding best practices for social scientists in this old article by Jonathan Nagler (1995) - [__Coding Style and Good Computing Practices__](http://www.jstor.org/stable/420315) - providing  very useful advice on coding as related to ETL and data analysis. Still incredibly relevant advice. If you only have a few minutes to skim, that  piece was more recently (2015) updated and summarized in a blog post - [__Writing Good Code__](https://blog.oup.com/2015/02/jonathan-nagler-writing-good-code/).

For more advanced hackers, you will benefit from a more systematic approach to improving your coding practices by reading a few more specialized pieces:

* [__The Practice of Programming__](http://www.informit.com/store/practice-of-programming-9780201615869), per Jonathan's recommendation read the Preface, Chapters 1, 3, 5, 6, and the Epilogue
* [__The Structure and Interpretation of Computer Programs__](https://mitpress.mit.edu/sicp/full-text/book/book.html) to better understand object-oriented languages, and
* [__The Pragmatic Programmer__](https://www.amazon.com/dp/020161622X/ref=cm_sw_su_dp?tag=devtools-20) with general advice on how to be a good programmer/coder

### Coding Style in Python

Nothing is more satisfying for a Python devotee than coming across code crafted in the correct "Pythonic" way. Not a hard thing to achieve since the community has produced a comprehensive document that leads the way - [__PEP 8 Style Guide for Python Code__](https://www.python.org/dev/peps/pep-0008/). Be nice to your fellow Pythonistas - and your future self - and learn it by heart.

### Coding Style in R

A lot of knowledge has been accumulated over the last years and systematized in coding style rules by the RStudio folks. For a book-version, you may want to read [Hadley Wickham](http://hadley.nz/)'s  chapters on [R code](http://r-pkgs.had.co.nz/r.html) and [Code Style](http://r-pkgs.had.co.nz/style.html) from his [__R Packages__](http://r-pkgs.had.co.nz) book. You may also want to go directly to the [`tidyverse` style guide](https://style.tidyverse.org) that contains best practices followed by all developers working on the `tidyverse`. (_Useless Random Fact:_ While the guide itself was originally an evolution from an older [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml), Google has now adopted the [`tidyverse` style guide](https://style.tidyverse.org) as its own).


### Commenting your git commits

Unless you are a seasoned developer, it may not be obvious why or how to comment a git `commit`. Fortunately, Chris Beams (2014) wrote a very nice post - [__How to Write a Git Commit Message__](https://chris.beams.io/posts/git-commit/) - that provides much needed guidance and advice on the appropriate way to write `commit` messages.
