/**
 * check_cycle - Function that checks if a singly linked list has a cycle
 * @list: pointer to the first element in a list
 *
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	struct listint_s *temp = malloc(sizeof(struct listint_s *next));

	temp = list->next;

	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
		{
			free temp;
			return (1);
		}
	}
	free temp;

	return (0);
}
