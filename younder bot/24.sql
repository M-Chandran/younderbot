select max(salary)as salary 
from employee 
order by salary desc
limit 3 offset 1;