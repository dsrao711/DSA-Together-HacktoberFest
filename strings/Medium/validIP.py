import string

class Solution(object):
    # Check IPV4            
    def checkIPV4(self , ip):
        # Get the digits
        for i in ip.split('.'):
            if len(i) > 3 or len(i) == 0:
                return False
            # Check if all are numbers
            # Check the numbers range
            # Check 0's condition 
            if((i[0] == '0' and len(i) != 1 ) or (not i.isdigit()) or int(i) > 255):
                return False
    
        return True    
        
    def checkIPV6(self , ip):
        for i in ip.split(':'):
            if(len(i) > 4 or len(i) == 0):
                return False
            # Check if all are hexadec
            else:
                if(not all(c in string.hexdigits for c in i)):
                    return False
        return True
        
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        
        if(queryIP.count('.') == 3):
            if(self.checkIPV4(queryIP)):
                return "IPv4"
            else:
                return "Neither"
        elif(queryIP.count(':') == 7):
            if(self.checkIPV6(queryIP)):
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
            