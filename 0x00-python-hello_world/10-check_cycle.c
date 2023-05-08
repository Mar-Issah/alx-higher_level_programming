#include "lists.h"

/**
 * check_cycle - find a loop in a list
 * @list: points to the start of the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
