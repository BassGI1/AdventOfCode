#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DISK_LENGTH_1 272
#define DISK_LENGTH_2 35651584

char *dragon_curve(char *state, int *current_len, int max_len)
{
	int len = *current_len;

	int new_len = len * 2 + 1;
	char *next_state = malloc(new_len + 1);

	memcpy(next_state, state, len);

	next_state[len] = '0';

	for (int i = 0; i < len; i++)
	{
		char bit = state[len - 1 - i];
		next_state[len + 1 + i] = (bit == '0') ? '1' : '0';
	}

	next_state[new_len] = '\0';
	free(state);

	*current_len = new_len;
	return next_state;
}

char *checksum(char *state, int *current_len)
{
	int len = *current_len;
	int new_len = len / 2;
	char *next_checksum = malloc(new_len + 1);

	for (int i = 0; i < new_len; i++)
	{
		char bit1 = state[i * 2];
		char bit2 = state[i * 2 + 1];

		next_checksum[i] = (bit1 == bit2) ? '1' : '0';
	}

	next_checksum[new_len] = '\0';
	free(state);

	*current_len = new_len;
	return next_checksum;
}

void solve(const char *initial_input, int target_length, int part)
{
	int curr_len = strlen(initial_input);

	char *disk = malloc(curr_len + 1);
	strcpy(disk, initial_input);

	while (curr_len < target_length)
	{
		disk = dragon_curve(disk, &curr_len, target_length);
	}

	disk[target_length] = '\0';
	curr_len = target_length;

	while (curr_len % 2 == 0)
	{
		disk = checksum(disk, &curr_len);
	}

	printf("Part %d Answer: %s\n", part, disk);
	free(disk);
}

int main()
{
	FILE *file = fopen("./input.txt", "r");

	char raw_input[256];
	raw_input[strcspn(raw_input, "\r\n")] = '\0';

	solve(raw_input, DISK_LENGTH_1, 1);
	solve(raw_input, DISK_LENGTH_2, 2);

	return 0;
}
