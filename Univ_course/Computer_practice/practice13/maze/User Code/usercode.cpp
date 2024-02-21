#include <stdlib.h>
#include "..\ExternDoc.h"
#include "..\UI\Zoom.h"
#include "..\UI\MsgView.h"
#include "..\Graphics\DrawFunc.h"
#include "..\Example\Example.h"

#define ERROR_NUMBER -1

//function prototype

static void drawDirect(CDC *pDC);
static void drawBuffered();

//Start of user code
#include <float.h>

/*****************************************************************
* function	: bool readFile(const char* filename)
* argument	: cons char* filename - filename to be opened
* return	: true if success, otherwise flase
* remark	: After read data file, phisycal view must be set;
*			  otherwise drawing will not be executed correctly.
*			  The window will be invalidated after readFile()
*			  returns true.
******************************************************************/
typedef struct node{
	int row;
	int col;
	bool right;
	bool down;
}node;
typedef struct list{
	struct node *Node;
	struct list *next;
}list;

list *last_ptr=NULL;
list* queue=NULL;
node** maze;

void push(node* nd){
	list* temp;

	if(last_ptr==NULL){
		queue=(list*)malloc(sizeof(list));
		last_ptr=queue;
		queue->Node=nd;
	}
	else{
		temp=(list*)malloc(sizeof(list));
		temp->Node=nd;
		last_ptr->next=temp;
		last_ptr=temp;
	}
	return;
}
node* pop(list** Q){
	node *temp;
	list* q;

	temp=(*Q)->Node;
	q=*Q;
	if((*Q)->next==NULL){
		*Q=NULL;
		last_ptr=NULL;
	}
	else{
		*Q=(*Q)->next;
	}
	free(q);
	return(temp);
}
int width;
int height;
bool readFile(const char* filename){
	
	//start of the user code
	bool flag=true;
	FILE *fp;
	fp=fopen(filename,"r");
	if(fp==NULL){
		flag=false;
		return flag;
	}
	node *temp;
	int i=0,j=0;
	width=0;
	char ch;
	last_ptr=NULL;
	queue=NULL;
	while(1){
		fscanf(fp,"%c",&ch);
		j++;
		if(j==1&&(ch!='|'&&ch!='+')){
			break;
		}
		if(ch=='\n'){
			if(i!=0&&i%2==0){
				node *puttemp;
				puttemp=temp;
				push(puttemp);
			}
			i++;
			j=0;
			continue;
		}
		if(i==0){
			if(ch=='-'){
				width++;
			}
			continue;
		}
		if(i%2==1){
			if(j==1){
				temp=(node*)malloc(sizeof(node)*width);	
				continue;
			}
		}

		if(i%2==1){
			int putcol;
			if(j%2==1){
				if(ch==' '){
					putcol=(j-2)/2;
					temp[putcol].right=true;
					temp[putcol].row=(i-1)/2;
					temp[putcol].col=putcol;
				}
				else if(ch=='|'){
					putcol=(j-2)/2;
					temp[putcol].right=false;
					temp[putcol].row=(i-1)/2;
					temp[putcol].col=putcol;
				}
			}
			else continue;

		}
		if(i%2==0){
			int putcol;
			if(j%2==0){
				if(ch==' '){
					putcol=(j-1)/2;
					temp[putcol].down=true;
					temp[putcol].row=(i-1)/2;
					temp[putcol].col=putcol;
				}
				else if(ch=='-'){
					putcol=(j-1)/2;
					temp[putcol].down=false;
					temp[putcol].row=(i-1)/2;
					temp[putcol].col=putcol;
				}
			}
			else continue;

		}
	}
	
	fclose(fp);

	height=i/2;

	maze=(node**)malloc(sizeof(node*)*height);
	for(int k=0;k<height;k++){
		maze[k]=pop(&queue);
	}
	setWindow(0,0,4*width+5,4*height+5,0);
	return true; //edit after finish this function
	//end of usercode
}

/******************************************************************
* function	: bool FreeMemory()
*
* remark	: Save user data to a file
*******************************************************************/
void freeMemory(){
	//start of the user code

	int i,j;
	if(maze!=NULL){
		for(i=0;i<height;i++){
			free(maze[i]);
		}
		free(maze);
		maze=NULL;
	}
	//end of usercode
}

/**************************************************************
* function	: bool writeFile(const char* filename)
*
* argument	: const char* filename - filename to be written
* return	: true if success, otherwise false
* remark	: Save user data to a file
****************************************************************/
bool writeFile(const char* filename){
	//start of the user code
	bool flag;
	flag = 0;

	return flag;
	//end of usercode
}

/************************************************************************
* fucntion	: void drawMain(CDC* pDC)
*
* argument	: CDC* pDC - device context object pointer
* remark	: Main drawing function. Called by CMFC_MainView::OnDraw()
*************************************************************************/
void drawMain(CDC *pDC){
	//if direct drawing is defined
#if defined(GRAPHICS_DIRECT)
	drawDirect(pDC);
	//if buffered drawing is defined
#elif defined(GRAPHICS_BUFFERED)
	drawBuffered();
#endif
}

/************************************************************************
* function	: static void drawDirect(CDC *pDC
*
* argument	: CDC* pDC - device context object pointer
* remark	: Direct drawing routines here.
*************************************************************************/
static void drawDirect(CDC *pDC){
	//begin of user code
	//Nothing to write currently.
	//end of user code
}

/***********************************************************************
* function	: static void drawBuffered()
*
* argument	: CDC* pDC -0 device object pointer
* remark	: Buffered drawing routines here.
************************************************************************/
static void drawBuffered(){
	//start of the user code
	list *ptr;
	node *V;
	int lineWidth = 0.01;
	int i,j;
	int x,y;
	//draw upper border
	DrawSolidBox_I(0,4*height,1,4*height+1,lineWidth,RGB(0,0,255),RGB(0,0,255));//가장 왼쪽 위 모서리
	for(i=0;i<width;i++){ //윗변
		DrawSolidBox_I(4*i+1,4*height,4*i+4,4*height+1,lineWidth,RGB(0,0,255),RGB(0,0,255));
		DrawSolidBox_I(4*i+4,4*height,4*i+5,4*height+1,lineWidth,RGB(0,0,255),RGB(0,0,255));
	}

	for(i=0;i<height;i++){//모든 열에 대하여 가장 왼쪽 벽을 그리고
		DrawSolidBox_I(0,4*(height-i)-3,1,4*(height-i),lineWidth,RGB(0,0,255),RGB(0,0,255));
		DrawSolidBox_I(0,4*(height-i-1),1,4*(height-i)-3,lineWidth,RGB(0,0,255),RGB(0,0,255));

		for(j=0;j<width;j++){//방을 한칸씩 읽으면서 오른쪽 방과 아래쪽 방과 연결 여부를 따져서 벽과 모서리를 그려나간다.
			if(maze[i][j].right ==false)
				DrawSolidBox_I(4*(j+1),4*(height-i)-3,4*j+5,4*(height-i),lineWidth,RGB(0,0,255),RGB(0,0,255));
			if(maze[i][j].down == false)
				DrawSolidBox_I(4*j+1,4*(height-i-1),4*(j+1),4*(height-i)-3,lineWidth,RGB(0,0,255),RGB(0,0,255));
			DrawSolidBox_I(4*(j+1),4*(height-i-1),4*j+5,4*(height-i)-3,lineWidth,RGB(0,0,255),RGB(0,0,255));
		}
	}
	//end of the user code
}

void DFS(){};
void BFS(){};