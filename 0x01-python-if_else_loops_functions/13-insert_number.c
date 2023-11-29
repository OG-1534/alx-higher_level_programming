#include "lists.h"
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert num in a sorted list
 *
 * @head: linked list
 * @number: num to insert
 *
 * Return: pointer to head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current = *head;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new != NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new;
		new->next = current;
	}
	return (new);
}
