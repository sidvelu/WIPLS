#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int file;
char *filename = "/dev/i2c-1";
int magAddr = 0x1E;


int main()
{
	if ((file = open(filename, O_RDWR)) < 0)
	{
		/* ERROR HANDLING: you can check errno to see what went wrong */
		perror("Failed to open the i2c bus");
    		exit(1);
	}

	if (ioctl(file, I2C_SLAVE, magAddr) < 0) 
	{
		printf("Failed to acquire bus access and/or talk to slave.\n");
		/* ERROR HANDLING; you can check errno to see what went wrong */
    		exit(1);
	}
	
	unsigned char buf[10] = {0};
	buf[0] = 0x00;
	
	int i;
 
	for (i = 0; i<5; i++) 
	{
    	// Using I2C Read
		if (read(file,buf,1) != 1) 
		{
        		/* ERROR HANDLING: i2c transaction failed */
			printf("Failed to read from the i2c bus: %s.\n", strerror(errno));
            		printf("\n\n");
		} 
		else 
		{
			printf(" Buffer: %X \n",  buf[0]);
        	/* Device specific stuff here */

		}
	}


	//Turning on MAG
	buf[0] = 0x02;
	buf[1] = 0x00;

	if(write(file, buf, 2) != 2)
	{
		printf("ERROR \n");
	}
	buf[0] = 0x02;
	
	if (read(file,buf,1) != 1) 
	{
        	/* ERROR HANDLING: i2c transaction failed */
		printf("Failed to read from the i2c bus: %s.\n", strerror(errno));
            	printf("\n\n");
	}
	else
	{
		printf(" Register 0x00: 0x%X \n", buf[0]);
	}
	
	
}
