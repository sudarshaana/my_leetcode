class Solution:
    def reformatDate(self, date: str) -> str:
        
    
        months = list(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    
    
        year = date[-4:]
        print(year)

        month = date[-8:-5]
        #print(month)

        month_start = date.find(month)
        day = date[0:month_start-3]
        #print(day)

        final_output = year+"-" + str(months.index(month)+1).zfill(2)+"-"+day.zfill(2)
        return final_output