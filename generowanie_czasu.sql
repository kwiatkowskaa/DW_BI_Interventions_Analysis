DECLARE @Year INT = 2014;

DECLARE @StartDate DATE = CAST(CAST(@Year AS VARCHAR) + '-01-01' AS DATE);
DECLARE @EndDate DATE = CAST(CAST(@Year AS VARCHAR) + '-12-31' AS DATE);

;WITH DateSequence AS (
    SELECT CAST(@StartDate AS DATETIME) AS DateValue
    UNION ALL
    SELECT DATEADD(MINUTE, 1, DateValue)
    FROM DateSequence
    WHERE DateValue < DATEADD(DAY, 1, @EndDate)
)
INSERT INTO DIM_CZAS (
    DATE,
    DATETIME,
    HOUR,
    MINUTE,
    DAY_NUMBER,
    DAY_SUFFIX,
    WEEK_DAY_NUMBER,
    WEEK_DAY_NAME,
    WEEKEND_FLAG,
    HOLIDAY_TEXT,
    HOLIDAY_FLAG,
    DAY_OF_YEAR_NUMBER,
    WEEK_OF_MONTH_NUMBER,
    WEEK_OF_YEAR_NUMBER,
    ISO_WEEK_OF_YEAR_NUMBER,
    MONTH_NUMBER,
    MONTH_NAME,
    QUARTER_NUMBER,
    QUARTER_NAME,
    YEAR_NUMBER
)
SELECT 
    CAST(DateValue AS DATE),
    DateValue,
    DATEPART(HOUR, DateValue),
    DATEPART(MINUTE, DateValue),
    DAY(DateValue),
    CAST(DAY(DateValue) AS VARCHAR) + 
        CASE 
            WHEN DAY(DateValue) IN (11,12,13) THEN 'th'
            WHEN DAY(DateValue) % 10 = 1 THEN 'st'
            WHEN DAY(DateValue) % 10 = 2 THEN 'nd'
            WHEN DAY(DateValue) % 10 = 3 THEN 'rd'
            ELSE 'th'
        END,
    DATEPART(WEEKDAY, DateValue),
    DATENAME(WEEKDAY, DateValue),
    CASE WHEN DATEPART(WEEKDAY, DateValue) IN (1, 7) THEN 'YES' ELSE 'NO' END,
    N'',
    'NO',
    DATEPART(DAYOFYEAR, DateValue),
    (DAY(DateValue) - 1) / 7 + 1,
    DATEPART(WEEK, DateValue),
    DATEPART(ISO_WEEK, DateValue),
    MONTH(DateValue),
    DATENAME(MONTH, DateValue),
    DATEPART(QUARTER, DateValue),
    'Q' + CAST(DATEPART(QUARTER, DateValue) AS VARCHAR),
    YEAR(DateValue)
FROM DateSequence
OPTION (MAXRECURSION 0);

