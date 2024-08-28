#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - endless loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - zombies
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t myp_id;

	for (i = 0; i < 5; i++)
	{
		myp_id = fork();
		if (myp_id)
			printf("Zombie process created, PID: %i\n", myp_id);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
