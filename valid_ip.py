# practice validate ip without regex

  def validIPAddress(IP):
      """
      :type IP: str
      :rtype: str
      """
      def valid_ipv4(IP):
          segement = IP.split('.')
          if len(segement) == 4:
              for s_str in segement:
                  if 0 < len(s_str) < 4:
                      for s in s_str:
                          if not s.isdigit():
                              return False
                      if len(s_str) > 1 and s_str[0] == '0' or int(s_str) > 255:
                          return False
                  else:
                      return False
          else:
              return False

          return True


      def valid_ipv6(IP):
          set_chars = '0123456789abcdefABCDEF'
          segement = IP.split(':')
          if len(segement) == 8:
              for seg_str in segement:
                  if 0 < len(seg_str) < 5:
                      for s in seg_str:
                          if s not in set_chars:
                              return False
                      
                      # make sure no multi '0'
                      not sure why test case didn't check '0000'
                      if len(seg_str) > 1 and seg_str[0] == '0' and seg_str[1] == '0':
                          print(2)
                          return False

                  else:
                      return False

          else:
              return False

          return True


      if valid_ipv4(IP):
          return "IPv4"

      if valid_ipv6(IP):
          return "IPv6"

      return "Neither"
        
if __name__ == '__main__':
    IP = ''
    validIPAddress(IP)
  
