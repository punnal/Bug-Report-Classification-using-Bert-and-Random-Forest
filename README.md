# Bug-Report-Classification-using-Bert-and-Random-Forest
## Catagory Classification using Bert
To run Bert for catagory classification run notebook `bugreport_Bert_Catagory.ipynb`. Change the dataset variable in the notebook to use `your_dataset.csv` or `paraphrased_catagory_full.csv`(These are more summaries generated using GPT 3.5 model)
To use oversampling change the value of the sampling variable in document to "o"
To use undersampling change the value of the sampling variable in document to "u"
To use the weighted loss function technique use the MyBertForSequenceClassification class at the end when initiating your model.
## Priority Classification using Bert
To run Bert for priority classification run notebook `bugreport_Bert_Priority.ipynb`. Change the dataset variable in the notebook to use `priority_dataset.csv` or `paraphrased_priority_full.csv`(These are more summaries generated using GPT 3.5 model)
To use oversampling change the value of the sampling variable in document to "o"
To use undersampling change the value of the sampling variable in document to "u"
To use the weighted loss function technique use the MyBertForSequenceClassification class at the end when initiating your model.
## Catagory Classification using Random Forest
To run Random Forest for catagory classification run notebook `Bugreport_random_forest_catagory.ipynb`. Change the dataset variable in the notebook to use `your_dataset.csv`.
To not use SMOTE comment it out from the code and uncomment the line `#X_res, y_res = X, y`
## Priority Classification using Random Forest
To run Random Forest for priority classification run notebook `Bugreport_random_forest_priority.ipynb`. Change the dataset variable in the notebook to use `priority_dataset.csv`.
To not use SMOTE comment it out from the code and uncomment the line `#X_res, y_res = X, y`
