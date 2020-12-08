#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *new_node = NULL;

	if (head == NULL)
		exit(1);
	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		exit(1);
	new_node->n = number;
	new_node->next = NULL;
	while (temp->next)
	{
		if (temp->next->n > number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}
		temp = temp->next;
	}
	return (new_node);
}
