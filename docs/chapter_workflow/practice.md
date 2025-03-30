# Reproducible Research 

This is a brief introduction on common practices for reproducible research.<br>
For a more detailed and free course please audit this [free course](https://www.edx.org/learn/data-science/harvard-university-principles-statistical-and-computational-tools-for-reproducible-data-science?index=product&queryID=cfa3fcc1b8bfd788f812d2526c322707&position=2) by Harvard.

**Reproducible Research** is a scientific approach where the data, computational methods, and results of a study are made available in sufficient detail to allow others (or the original researchers at a later time) to independently verify findings, repeat analyses, and build upon previous work.

## Store your raw data in a separate folder and never change it

This ensures that everyone has the same beginning of the analysis as you!

## Informative naming variables
- Make sure that your variable name is easy to understand and reflect directly its content<br>
- Avoid general terms like `test`, `test1`, ...<br>
- This will improve the readability of your code<br>
**Bad example**<br>
```r
# Analyzing patient data
test <- read.csv("data.csv")
stuff <- test[test$group == "treatment", ]
final <- mean(stuff$bloodpressure)
x <- sd(stuff$bloodpressure)
result2 <- final/x
y <- stuff[stuff$age > 40, ]
z <- mean(y$bloodpressure)
```
**Good example**<br>
```r
# Analyzing patient data
patient_data <- read.csv("data.csv")
treatment_group <- patient_data[patient_data$group == "treatment", ]
mean_blood_pressure <- mean(treatment_group$bloodpressure)
blood_pressure_sd <- sd(treatment_group$bloodpressure)
standardized_bp <- mean_blood_pressure/blood_pressure_sd
older_patients <- treatment_group[treatment_group$age > 40, ]
mean_bp_older_patients <- mean(older_patients$bloodpressure)
```

## Overcommenting
Most of the time, your code makes perfect sense for you ... when you write it. But visiting it after a year is another story. I cannot stress how much time I wasted figuring out what was my past self thinking. Therefore, always overcomment things!<br>

A tip: Put yourself in the position of someone who will read your code without knowing too much about the project<br>

These comments should:<br>
1. Provides context about the analysis purpose<br>
2. Explains data content and processing decisions<br>
3. Describes what diagnostics are checking and why<br>

**Bad example**<br>
```r
# Read the CSV file
df <- read.csv("clinical_trial.csv")  # Reading the CSV file

# Remove rows with missing values
df <- df[complete.cases(df), ]  # This removes rows with NA

# Calculate BMI
df$bmi <- df$weight / (df$height/100)^2  # BMI formula

# Create linear model
model <- lm(response ~ treatment + age + bmi + gender, data = df)  # Building model
```
**Good example**<br>
```r
# Clinical trial analysis examining treatment effect on blood pressure
# Dataset contains: patient demographics, treatment assignment, and outcomes
# Date: 2023-03-15, Author: P. Vu

# Remove subjects with missing data (10% of original sample)
# Decision made with PI to use complete case analysis instead of imputation
df <- read.csv("clinical_trial.csv")
df <- df[complete.cases(df), ]

# Calculate BMI - using height in cm converting to meters
# Formula: weight(kg) / height(m)^2
df$bmi <- df$weight / (df$height/100)^2

# Primary analysis: Effect of treatment on blood pressure response
# Adjusting for pre-specified covariates: age, BMI, gender
model <- lm(response ~ treatment + age + bmi + gender, data = df)

# Diagnostics for linear model assumptions
# Checking normality of residuals (required for valid p-values)
residuals <- model$residuals
hist(residuals, main="Histogram of Residuals", xlab="Residual Value")
qqnorm(residuals)
qqline(residuals)
shapiro_result <- shapiro.test(residuals)

# If p > 0.05, normality assumption is reasonable
print(paste("Shapiro-Wilk p-value:", shapiro_result$p.value))
```
## Version control
1. If you use Git, make a habit of commiting often
    - After each logical change:
        - Complete a function/analysis step
        - Fix a bug
        - Add a new feature
    - At the minimum, commit at the end of your work session
    - At any given point that you think you may want to return to
2. Most of your version control can be done via Git but it is always a good idea to add a time stamp to your deliverables like figures, tables. <br>
A good trick is to use the time function so you do not have to manually change the file name everytime you run.
```r
# Save the final figure
ggsave(paste0("../figures/", format(Sys.time(), "%Y_%m_%d"), "_intensify_fig_continuous_power_80.png"))
```
This code saves the file with the date it was created!
## Have a dry lab note
Use softwares like OneNote to document the process of your research. These includes:<br>
    - Summary of the papers you read<br>
    - Notes for your meetings<br>
You will never know if you have to go back to your old project!
## Be patient with yourself!
I must admit, I do not follow these rules 100% of the time.<br>
It is a skills and like every skills, it needs practice.<br>
As long as you are trying to be better! You will be better!<br>
Thank you!