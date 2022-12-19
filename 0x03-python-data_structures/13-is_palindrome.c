#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the pointer of the first node of the list
 *
 * Return: 0 if it's not a palindrome
 * 1 if it's a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp_p;
	int count = 1;
	int idx = 0;
	int idx2 = 0;

	if (*head == NULL)
		return (1);
	temp_p = malloc(sizeof(listint_t));
	temp_p = *head;
	while (temp_p->next != NULL)
	{
		temp_p = temp_p->next;
		count++;
	}
	int first_array[count];
	int reversed_array[count];

	temp_p = *head;
	while (temp_p != NULL)
	{
		first_array[idx] = temp_p->n;
		idx++;
		temp_p = temp_p->next;
	}
	while (idx >= 0)
	{
		reversed_array[idx2] = first_array[idx];
		idx--;
		idx2++;
	}
	while (idx2 >= 0)
	{
		if (reversed_array[idx2] != first_array[idx])
			return (0);
		idx2--;
		idx++;
	}
	return (1);
}
