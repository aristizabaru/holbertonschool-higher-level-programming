#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *new_node = NULL;

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (new_node);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp)
	{
		if (temp->next == NULL || temp->next->n >= number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}
		temp = temp->next;
	}
	return (new_node);
}
