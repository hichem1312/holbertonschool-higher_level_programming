#include "lists.h"
/**
 * check_cycle - check the list have a cycle or not
 * @list: list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	struct listint_s *cycle;
	if (list == NULL || list->next == NULL)
		return (0);
	cycle = list;
	while (list->next != NULL)
	{
		list = list->next;
	       if (cycle->next == list->next)
	       return (1);
	}
return (0);
}
