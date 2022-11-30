#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle
 * @list: pointer to the first element in a list
 *
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	temp = malloc(sizeof(listint_t));

	temp = list;

	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
		{
			return (1);
		}
	}

	return (0);
}
