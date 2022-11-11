# Reformat Date
class Solution:
    def reformatDate(self, date: str) -> str:
        month = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        D, M, Y = date.split(' ')
        return '-'.join([Y, month[M], D[:-2].rjust(2, '0')])


s = Solution()
print(s.reformatDate(date="20th Oct 2052"))
print(s.reformatDate(date="6th Jun 1933"))



# JavaScript Solution
# /**
#  * @param {string} date
#  * @return {string}
#  */
# var reformatDate = function(date) {
# let month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'};
# var [D, M, Y] = date.split(' ');
# return Y + '-' + month[M] + '-'+ D.slice(0,-2).padStart(2,'0');
# };