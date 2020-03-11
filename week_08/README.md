## WEEK 8 - Explanation vs Prediction

The __difference between explanation and prediction__ is an often overlooked topic in Data Science based on a widespread belief that _all  work in Data Science is strictly predictive_. This has become such a commonly held misconception that many use prediction as the sole characteristic to define the field.

It should be clear by now that the main skill of a Data Scientist is thinking critically about data, not treating every problem as a prediction problem. The reality is that no predictive work can consistently be good predictive work absent critical thinking about data. And understanding the difference between explanation and prediction is central to answering questions effectively and using data efficiently.

### How to think about this difference?

This is another area where the academic literature provides very useful guidance on ways to think about the difference between explanation and prediction.

One camp, best exemplified by Galit Shmueli's (2010) article - [__To Explain or To Predict?__](http://projecteuclid.org/download/pdfview_1/euclid.ss/1294167961) - poses that __explaining and predicting are two very different undertakings__ that follow different logics, employ different methods and produce different outputs. In her view, __the difference between explanatory and predictive models lies in measurement error__ :  

> Why should there be a difference between explaining and predicting? The answer lies in the fact that measurable data are not accurate representations of their underlying constructs. The operationalization of theories and constructs into statistical models and measurable data creates a disparity between the ability to explain phenomena at the conceptual level and the ability to generate predictions at the measurable level.

Perhaps her most acute point is that failing to recognize this difference creates, in practice, a confusion with far reaching consequences :

> A common misconception in various scientific fields is that predictive power can be inferred from explanatory power.  

The other camp, best exemplified by Leo Breiman's (2001) classical article - [__Statistical Modeling: The Two Cultures__](https://projecteuclid.org/download/pdf_1/euclid.ss/1009213726) - argues that __any difference between explanation and prediction results from a misguided reliance on data models__. This practice has led to a poor representation of reality

> Higher predictive accuracy is associated with more reliable information about the underlying data mechanism. Weak predictive accuracy can lead to questionable conclusions.

While valid under strict assumptions, Breiman's argument fails to recognize Shalit's point about measurement error and also the fact that explanatory (data) models are - and must be - simplifications of observed reality by construction. This last point is an epistemological one that dates back to Milton Friedman's (1966) insightful article - [__The Methodology of Positive Economics__](http://kimoon.co.kr/gmi/reading/friedman-1966.pdf) :

> A hypothesis is important is it "explains" much by little, that is if it abstracts the common and crucial elements from the mass of complex and detailed circumstances surrounding the phenomena to be explained and permits valid predictions on the basis of them alone. To be important, therefore, a hypothesis must be descriptively false in its assumptions.  

Explanation and prediction, therefore, cannot be the same exercises except under very specific circumstances.

### How to work with this difference?

Now that we have established the difference between explanation and prediction more clearly, it is also important to keep in mind some of the sharper wisdom that we have accumulated about predictive exercises and their departure/overlap with explanatory exercises. A trio of pieces by J Scott Armstrong - in the context of time-series forecasting - summarize much of the state of the art on prediction that is applicable across the board:

*  a (2001) chapter - [__Evaluating Forecasting Methods__](https://repository.upenn.edu/marketing_papers/146/?utm_source=repository.upenn.edu%2Fmarketing_papers%2F146&utm_medium=PDF&utm_campaign=PDFCoverPages) - that summarizes steps and principles to evaluate forecasts based on dense stack of academic research.
* a (2011) paper - [__Illusions in Regression Analysis__](https://repository.upenn.edu/cgi/viewcontent.cgi?article=1190&context=marketing_papers) - that illustrates the empirical differences between fitting models and generating predictions/forecasts
* a (2015) article with colleagues - [__Golden rule of forecasting: Be conservative__](https://www.sciencedirect.com/science/article/pii/S0148296315001459) - that compiles principles that summarize current knowledge on predicting/forecasting
