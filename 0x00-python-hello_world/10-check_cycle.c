#include "lists.h"
/**
 * check_cycle - check the list have a cycle or not
 * @list: list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *b, *a;

	if (list == NULL || list->next == NULL)
		return (0);
	b = list->next;
	a = list->next->next;

	while (b && a && a->next)
	{
		if (b == a)
			return (1);

		b = b->next;
		a = a->next->next;
	}
	return (0);
}
