-- creating a new database 
create database ds_jobs;
use ds_jobs;
select * from salaries;

/*1. You're a Compensation analyst employed by a multinational corporation. 
Your Assignment is to Pinpoint Countries who give work fully remotely, 
for the title 'managers’ Paying salaries Exceeding $90,000 USD.
*/
select distinct(company_location) as 'countries offering remote jobs' from salaries
where job_title like '%Manager%' and salary_in_usd > 90000 and remote_ratio = 100;


/*2.  AS a remote work advocate Working for a progressive HR tech startup 
who place their freshers’ clients IN large tech firms. 
You're tasked WITH Identifying top 5 Country 
Having greatest count of large (company size) number of companies.*/
select company_location, count(*) as 'count' 
from (
	select * from salaries
	where experience_level = 'EN' and company_size = 'L'
) t
group by company_location
order by count desc
limit 5;


/*3.  Picture yourself AS a data scientist Working for a workforce management platform.
 Your objective is to calculate the percentage of employees. 
 Who enjoy fully remote roles WITH salaries Exceeding $100,000 USD, 
 Shedding light ON the attractiveness of high-paying remote positions IN today's job market.
*/
set @COUNT= (SELECT COUNT(*) FROM salaries  WHERE salary_IN_usd >100000 and remote_ratio=100);
set @total = (SELECT COUNT(*) FROM salaries where salary_in_usd>100000);
set @percentage= round((((SELECT @COUNT)/(SELECT @total))*100),2);
SELECT @percentage AS '%  of people working remotely and having salary>100,000 USD';


/*4. Imagine you're a data analyst Working for a global recruitment agency. 
Your Task is to identify the Locations where entry-level average salaries exceed the 
average salary for that job title in market for entry level, 
helping your agency guide candidates towards lucrative countries.*/
SELECT company_location, t.job_title, average_per_country, average FROM 
(
	SELECT company_location,job_title,AVG(salary_in_usd) AS average_per_country FROM  salaries WHERE experience_level = 'EN' 
	GROUP BY  company_location, job_title
) AS t 
INNER JOIN 
( 
	SELECT job_title,AVG(salary_in_usd) AS average FROM  salaries  WHERE experience_level = 'EN'  GROUP BY job_title
) AS p 
ON  t.job_title = p.job_title WHERE average_per_country> average;


/*5. You've been hired by a big HR Consultancy to look at how much people get paid IN different Countries. 
Your job is to Find out for each job title which Country pays the maximum average salary. 
This helps you to place your candidates IN those countries.*/
SELECT company_locatiON , job_title , average FROM
(
SELECT *, dense_rank() over (partitiON by job_title order by average desc)  AS num FROM 
(
SELECT company_locatiON , job_title , AVG(salary_IN_usd) AS 'average' FROM salaries GROUP BY company_locatiON, job_title
)k
)t  WHERE num=1;


/*6.  AS a data-driven Business consultant, you've been hired by a multinational corporation to analyze 
salary trends across different company Locations. Your goal is to Pinpoint Locations WHERE 
the average salary Has consistently Increased over the Past few years 
(Countries WHERE data is available for 3 years Only(this and pst two years) 
providing Insights into Locations experiencing Sustained salary growth.*/

select * from salaries
where company_location in (
	select company_location from (
		select company_location, avg(salary_in_usd) as avg_salary, count(distinct work_year) as num_years
		from salaries
		where work_year >= year(current_date()) - 2
		group by company_location having num_years = 3
)m )


