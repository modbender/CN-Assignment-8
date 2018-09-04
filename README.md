# CN Assignment

## Assignment Question 08
**Modify UDP message to show the same checksum.**
Write a UDP Client program that sends some data to a UDP server on a specified port. The server echoes back the content received by duplicating it (e.g. if clients sends data as 'ABCD', the server will respond back with 'ABCDABCD'). For this  request sent and received response compute the checksum and display the same.  Verify your checksum computation by taking a TCP dump and displaying the same. Make a second request by appending 6 characters to original data to ensure that checksum remains the same. The first two characters of these 6 added characters should be first 4 characters of original input and remaining 4 characters you need to compute.

The program is to be invoked as
`./asn1_8 -s <server ip address> -p <server port number> -P <client port number> -d <data>`


## Members
- 1KS14CS076 Pavan Kumar D
- 1KS15CS091 Shanthanu S
- 1KS15CS121 Yashas H.R.
