#include "lists.h"
/**
 * insert_node - function that insertds a node in a
 * sorted list
 * @head: pointer to pointer to the first node
 * @number: datta to be stored in the inserted node
 *
 * Return: return the address of the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *current = NULL;
	listint_t *ptr = malloc(sizeof(listint_t));

	tmp = *head;
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;
	if (tmp == NULL)
		tmp = ptr;
	while(tmp != NULL)
	{
		current = tmp;
		if (number < tmp->n)
		{
			current->next = ptr;
			ptr->next = tmp;
			break;
		}
		else
			continue;
		tmp = tmp->next;
	}
	if (tmp == NULL)
		tmp->next = ptr;
	return (ptr);
}
