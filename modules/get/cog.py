from discord.ext import commands
from zipfile import ZipFile
import discord
import glob
import os

class Get(commands.Cog, name="Download"):
    """For Downloading listed files"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def get(self, ctx: commands.Context, lab, week=None, problem=None):
        """
        Get the .pdf files for the desired problem

        Example: 
        `haya get BG75 3 A`
        `haya get BG75 5` on progress(not yet available)
        `haya get BG75` on progress(not yet available)
        `haya get all`
        """
        def get_all_file_paths(directory):
        
            # initializing empty file paths list
            file_paths = []
        
            # crawling through directory and subdirectories
            for root, directories, files in os.walk(directory):
                for filename in files:
                    # join the two strings in order to form the full filepath.
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
        
            # returning all file paths
            return file_paths            

        def bulking():
            # path to folder which needs to be zipped
            directory = './problems'
        
            # calling function to get all file paths in the directory
            file_paths = get_all_file_paths(directory)
            file_paths.sort()
        
            # # printing the list of all files to be zipped
            # for file_name in file_paths:
            #     print(file_name)
        
            # writing files to a zipfile
            with ZipFile('./problems/problems-' + temp  +'.zip','w') as zip:
                print('Following files will be zipped:')
                # writing each file one by one
                for file in file_paths:
                    if lab != 'ALL':
                        if file.find(lab) != -1 and file.find('week-' + week): 
                            print(file)
                            zip.write(file)
                        elif file.find(lab) != -1:
                            print(file)
                            zip.write(file)
                        else: continue
                    else:
                        print(file)
                        zip.write(file)


            print('All files zipped successfully!') 

        if lab == 'ALL':
            temp = lab.upper
            temp.upper()
        elif lab and week:
            temp = lab + '-' +str(week)    
            temp.upper()
        elif lab:
            temp = lab
            temp.upper()

        if lab == 'ALL':
            print("all")
            if os.path.exists('./problems/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
            else:
                bulking()  
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
        elif lab and week and problem:
            problem = problem.upper()
            lab = lab.upper()
            file_path = glob.glob("./problems/*/" + lab + '-week-' + week + '-prob-' + problem + '.pdf')
            
            await ctx.send(file=discord.File(file_path[0]))
        elif lab and week:
            print("lab and week")
            if os.path.exists('./problems/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
            else:
                bulking()  
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
        elif lab:
            print("lab")
            if os.path.exists('./problems/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
            else:
                bulking()  
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))


async def setup(bot: commands.Bot):
    await bot.add_cog(Get(bot))