#include "lists.h"
#include <stdlib.h>
/**
* insert_node - inserts a num into a sorted singly linked list
* @head: points to the list
* @number: the number to insert
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *new_loc = *head;

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!new_loc || new->n < new_loc->n)
	{
		new->next = new_loc;
		*head = new;
		return (*head);
	}

	while (new_loc)
	{
		if (!new_loc->next || new->n < new_loc->next->n)
		{
			new->next = new_loc->next;
			new_loc->next = new;
			return (new_loc);
		}
		new_loc = new_loc->next;
	}

	return (NULL);
}
