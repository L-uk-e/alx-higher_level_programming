#include "lists.h"

/**
 * insert_node - Inserts a number into a singly linked list
 * @head: Pointer to the head of the list
 * @number: number to be inserted as the data
 *
 * Return: Pointer to the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *new = malloc(sizeof(listint_t));

	temp = *head;

	while (temp != NULL)
	{
		if(temp->next->n < number)
		{
			temp = temp->next;
		}
		else
		{
			new->n = number;
			new->next = temp->next;
			temp->next = new;
			break;
		}
	}

	if (temp == NULL)
	{
		return (NULL);
	}

	return (new);
}
