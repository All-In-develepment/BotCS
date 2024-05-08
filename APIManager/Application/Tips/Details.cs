using Application.Core;
using Application.Interfaces;
using AutoMapper;
using AutoMapper.QueryableExtensions;
using Domain;
using MediatR;
using Microsoft.EntityFrameworkCore;
using Persistence;

namespace Application.Tips
{
    public class Details
    {
        public class Query : IRequest<Result<TipDto>>
        {
            public int Id { get; set; }
        }

        public class Handler : IRequestHandler<Query, Result<TipDto>>
        {
            private readonly DataContext _context;
            private readonly IMapper _mapper;

            public Handler(DataContext context, IMapper mapper)
            {
                _mapper = mapper;
                _context = context;
            }

            public async Task<Result<TipDto>> Handle(Query request, CancellationToken cancellationToken)
            {
                var tip = await _context.Tips
                    .ProjectTo<TipDto>(_mapper.ConfigurationProvider)
                    .FirstOrDefaultAsync(x => x.TipId == request.Id);

                return Result<TipDto>.Success(tip);
            }
        }
    }
}