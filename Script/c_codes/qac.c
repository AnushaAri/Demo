#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<regex.h>
#include<xlsxwriter.h>
#define F_NAME "Input.txt"
#define MATCH ":[0-9]"
#define MODE "r"

int compare(char *file_name, char *search, char *lvl);
void create_sheet();
void write_sheet(char **id);

void main()
{
  char level[10];
  char filename[30];
  char to_find[30];

  printf("Enter input filename: ");
  scanf("%s", filename);
  printf("Enter warning level: ");
  scanf("%s", level);
  strcat(level, MATCH);  
  strcpy(to_find, level);  
  compare(filename, to_find, level);
  create_sheet();
}

int compare(char *file_name, char *search, char *lvl) 
{
  regex_t re;
  FILE *fp;
  char line[1000];
  int retval = 0;
  char *token, *pat;  
  char *Ids[2];
  int i = 0, j = 0;
 
  fp = fopen(file_name, MODE);

  if (fp == NULL)
  {
    perror(file_name);
    exit(0);
  }
  retval = regcomp(&re, search, REG_EXTENDED);
  printf("retval %d\n", retval);

  if (retval)
  {
    printf("Failed to complete regex '%s'\n", search);
    exit(0);
  }

  i = 0;
  retval = 0;
  while(fgets(line, sizeof(line), fp) != NULL)
  {
    line[strlen(line) - 1] = '\0';
    retval = regexec(&re, line, 0, NULL, 0);
    printf("retval %d\n", retval);


/*    if (0 != retval)
    {
      exit(0);
    }
*/
    if (retval)
    {
      printf("%s\n", line);
      token = strpbrk(search, ":");
      token = strtok(token, ":");
      printf("%s\n", token);
      strcpy(Ids[i], token);  
      printf("%s\n", Ids[i]);      
      i++;      
    }
    regfree(&re);
  }

//  write_sheet(&*Ids);
  fclose(fp);
  return 0;
}

void create_sheet()
{
  char excel_name[20];
  int row = 0;
  int col = 0;
  char *data[3] = {"Filename", "Level", "Warning ID"};

  printf("Enter excel sheet name: ");
  scanf("%s", excel_name);
  remove(excel_name);
  lxw_workbook *workbook = workbook_new(excel_name);
  lxw_worksheet *worksheet = workbook_add_worksheet(workbook, NULL);


  for (col=0; col<3 ; col++)
  {
    worksheet_write_string(worksheet, row, col, data[col], NULL);
  } 
  
  workbook_close(workbook);
}

void write_sheet(char **id)
{
  printf("sheet content\n");
  printf("%s\n", id[0]);
//  printf("%s\n", id[1]);
} 
